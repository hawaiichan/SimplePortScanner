import socket                                                                                                                                                                                                                              

#ポートの範囲を設定
max_port = 65535                                                                                                                                                                                                                           
min_port = 1    

print("IPアドレスを入れてください")                                                                                                                                                                                                        
target_host = input(":")                                                                                                                                                                                                                   

#ここでポートをスキャンする
for port in range(min_port, max_port):                                                                                                                                                                                                     
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                                                                                                                                                                               
    return_code = sock.connect_ex((target_host, port))                                                                                                                                                                                     
    sock.close()                                                                                                                                                                                                                           

#開いているポートを見つけたら0を返す
    if return_code == 0:                                                                                                                                                                                                                   
        print("Port %d open!" % (port))                                                                                                                                                                                                    
                                                                                                                                                                                                                                           
print("Complete!")                                                                                                                                                                                                                         
                     
