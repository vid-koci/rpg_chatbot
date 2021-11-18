import torch,transformers
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
  
class chatbot:
    def __init__(self):
        self.prompts = {"armor":"This story is happening in a Room, Inside Witch's Tower. The walls are tall and made of stone. The walls of the room are barren except of a carpet on the floor. In front of you enters a (P1). The animated armor thinks \"I guard the laboratory of witch Glinidril. I will guard the door against anyone who is not a friend of Glinidril or Glinidril herself. I will hit anyone else.\" Description of carpet : Beautiful red carpet which is alive and will attack on armor's command. Description of (P1) : (P1_desc) |", "Glinidril":"This story is happening in Witch's Laboratory, Inside Witch's Tower. The walls are tall and made of stone. The large room contains several large tables, lab items, and a colorful gem that casts light. The room is entered by (P_names). On the other side of the hall stand a grey and a white knight. The witch thinks \"I am witch Glinidril. I must protect the gem at all costs. I am a mighty witch and can cast powerful spells. Visitors in this room look suspicious to me and if they threaten taking my gem, I will hit them.\" Description of the gem : The gem is of a size of an apple and sheds beautiful blue light. Description of a grey knight : in grey armor and armored with a huge sword. Description of a white knight : in shining white armor and armored with a huge sword. (P_descriptions) |"}

    def initialize(self, characters, speaker):
        self.characters = characters
        self.speaker=speaker
        self.device="cpu"
        self.tokenizer = AutoTokenizer.from_pretrained("t5-large")
        self.model = AutoModelForSeq2SeqLM.from_pretrained("chatbot_trained")
        self.model.eval()
        assert len(self.characters)>0
        self.body = self.prompts[speaker].replace("(P1)",characters[0][0]).replace("(P1_desc)",characters[0][1])
        if len(self.characters) == 1:
            all_names = characters[0][0]
        else:
            all_names = ", ".join([c[0] for c in characters])+", and "+characters[-1][0]
        all_descriptions = " ".join(["Description of "+c[0]+" : "+c[1] for c in characters])
        self.body = self.body.replace("(P_names)",all_names).replace("(P_descriptions)",all_descriptions)
        return self.body.replace("|","\n")

    def pad_and_truncate(self,batch,padding=0):
        max_size = self.tokenizer.model_max_length
        pipe_id = self.tokenizer.encode("|")[0]
        batch_len = 0
        for i in range(len(batch["input_ids"])):
            if pipe_id in batch["input_ids"][i]:
                pipe_location = batch["input_ids"][i].index(pipe_id)
                if pipe_location>max_size*2//3:#if the scene description is a bit too long, cut the last part
                    scene_description=batch["input_ids"][i][:max_size*2//3]+[pipe_id]
                    scene_description_attention=batch["attention_mask"][i][:max_size*2//3]+[batch["attention_mask"][i][pipe_location]]
                else:
                    scene_description = batch["input_ids"][i][:pipe_location+1]
                    scene_description_attention = batch["attention_mask"][i][:pipe_location+1]
                conversation = batch["input_ids"][i][pipe_location+1:]
                conversation_attention = batch["attention_mask"][i][pipe_location+1:]
                if len(scene_description)+len(conversation)>max_size:#truncate the front of conversation if need be
                    batch["input_ids"][i]=scene_description+conversation[len(scene_description)+len(conversation)-max_size:]
                    batch["attention_mask"][i]=scene_description_attention+conversation_attention[len(scene_description)+len(conversation)-max_size:]
                else:
                    batch["input_ids"][i]=scene_description+conversation
                    batch["attention_mask"][i]=scene_description_attention+conversation_attention
            else:
                if len(batch["input_ids"][i])>max_size:
                    batch["input_ids"][i]=batch["input_ids"][i][:max_size]
                    batch["attention_mask"][i]=batch["attention_mask"][i][:max_size]
            batch_len = max(batch_len,len(batch["input_ids"][i]))
        return_ids = torch.ones(len(batch["input_ids"]),batch_len,dtype=torch.long)*padding
        return_attention = torch.zeros(len(batch["input_ids"]),batch_len,dtype=torch.long)
        for i in range(len(batch["input_ids"])):
            for j in range(len(batch["input_ids"][i])):
                return_ids[i][j]=batch["input_ids"][i][j]
                return_attention[i][j]=batch["attention_mask"][i][j]
        batch["input_ids"]=return_ids
        batch["attention_mask"]=return_attention
        return batch

    def query(self, added_text):
        self.body = self.body+" "+added_text+ " "+{"armor":"animated armor", "Glinidril":"witch"}[self.speaker]
        inputs = self.pad_and_truncate(self.tokenizer([self.body])).to(self.device)
        predictions = self.model.generate(inputs["input_ids"],max_length=128)
        generated_text = self.tokenizer.decode(predictions[0],skip_special_tokens=True)
        self.body+= " "+generated_text
        return {"armor":"animated armor", "Glinidril":"witch"}[self.speaker]+" "+generated_text
