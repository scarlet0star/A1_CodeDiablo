
def screen_output(stage_num):    
    from utils import load_files 
    sector = load_files("sector.json")

    stage_text = sector[stage_num]
    print(stage_text["place_name"] if stage_text["place_name"] != None else "") # 이 부분 수정 필요?

    return stage_text["place_name"]

a = screen_output(0)
print(a)