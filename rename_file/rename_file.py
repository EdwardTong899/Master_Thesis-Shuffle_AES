import os

# 設定起始和結束的檔名
start_num = 5001
end_num = 9999

# 設定檔案的前綴和後綴
prefix = 'powerTrace'
suffix = '.out'

# 設定檔案路徑
old_path = 'Z:/LAB DATA/Presented_Papers/至/experiment_result2/'
new_path = 'Z:/LAB DATA/Presented_Papers/至/experiment_result2/'

# 循環處理檔案
for i in range(start_num, end_num + 1):
    # 舊檔案路徑
    old_file = old_path + prefix + str(i-5000) + suffix
    # 新檔案路徑
    new_file = new_path + prefix + str(i) + suffix
    # 使用os.rename()函數更改檔案路徑和名稱
    os.rename(old_file, new_file)
    print(i)
