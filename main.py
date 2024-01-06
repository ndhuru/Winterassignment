import os
import pandas as pd

#path to the folder containing the images
image_folder_path = 'C:\\Users\\narwh\\OneDrive\\Desktop\\PWP2022'

#path to the text file containing the new file names
text_file_path = os.path.join(image_folder_path, 'renamed_files.txt')

#create the text file with renamed names
#this will serve to help me rename the files in the folder alongside with directly putting the
#filenames in the excel instead of copying from the folder itself
with open(text_file_path, 'w') as file:
    for i in range(1, 2001):
        file.write(f'PWP2024_{i:07d}N_{i:04d}N_DHURUVA.JPG\n')

#read the new file names from the text file
with open(text_file_path, 'r') as file:
    new_file_names = [line.strip() for line in file]

#iterate over the files in the image folder and rename them
for index, old_file_name in enumerate(os.listdir(image_folder_path)):
    old_file_path = os.path.join(image_folder_path, old_file_name)
    new_file_path = os.path.join(image_folder_path, new_file_names[index])

    os.rename(old_file_path, new_file_path)

#make a dataframe with the new file names
data = {'New File Names': new_file_names}
df = pd.DataFrame(data)

#save the DataFrame to a CSV file
csv_file_path = os.path.join(image_folder_path, 'file_names.csv')
df.to_csv(csv_file_path, index=False)

#confirmation message
#i made this for debugging purposes
print("Files renamed and CSV file created successfully.")


#note: the csv file  will be created inside the folder with all the renamed files, that isn't against 
#of any the rules stated in the assignment.
