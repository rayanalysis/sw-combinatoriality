# whales
import os


with open('sperm-whale-dialogues.csv') as whale_expressions_data:
    whale_data = whale_expressions_data.read()
    
    line_count = 0
    out_v = open('clean_whale_data.txt','w')
    
    for line in whale_data.split(','):
        out_v.write(line + ' ')
        
    out_v.close()
    whale_expressions_data.close()
    
with open('clean_whale_data.txt') as whale_expressions_data:
    whale_data = whale_expressions_data.read()
    whale_recordings_list = []
    previous_filename = ''
    line_counter = 0
    filegroup_holder = []

    for line in whale_data.split('\n'):
        line_counter += 1
        sub_list = line.split(' ')
        
        if previous_filename == sub_list[0]:
            # print('A match!')
            filegroup_holder.append(sub_list)
            # print(filegroup_holder)
            
        else:
            if line_counter > 32:
                whale_recordings_list.append(filegroup_holder)
                filegroup_holder = []
        
        # print(previous_filename)
        previous_filename = sub_list[0]
        
    whale_expressions_data.close()
    
    for audio_recording in whale_recordings_list:
        try:
            record_name = audio_recording[0][0]
            out_v = open(record_name + '.txt','w')
            out_str = ''
            
            for sub_record in audio_recording:
                for data in sub_record:
                    out_str += data
                    out_str += ' '
                out_str += '\n'
                
            out_v.write(out_str)
            out_v.close()
            
        except:
            pass
