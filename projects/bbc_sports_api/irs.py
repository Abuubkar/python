import bbc_content_scrapper as bcs
import os
import re
import numpy as np

file_struc = "./data/news{0}.txt"


def run_irs():
    try:
        if (not os.path.exists('./data'))or (not os.path.exists("url.in")):
            bcs.get_content()
        elif(not os.stat("url.in").st_size == 0):
            bcs.get_content()
        elif(len(os.listdir('./data/')) == 0):
            bcs.get_content()

        print("Initiating IRS!! ...")
        # To check if file exist or not

        def file_exist(x): return os.path.exists(file_path(x))

        # To return exact file path

        def file_path(x): return file_struc.format(x)

        file_count = 1
        unique_words = ()
        data = ""
        while(file_exist(file_count)):  # looping while files are present
            with open(file_path(file_count)) as file:
                data += file.read().lower()
                file_count += 1

        data = re.sub('[^A-Za-z0-9 ]+', ' ', data)
        unique_words = sorted(set(data.split()))

        dictionary_matrix = dict()
        # matrix = array(29).reshape(file_count-1, len(unique_words))
        matrix = np.empty([file_count-1, len(unique_words)])

        file_count = 1
        while(file_exist(file_count)):  # looping while files are present
            with open(file_path(file_count)) as file:
                temp = file.read().lower()
                temp = re.sub('[^A-Za-z0-9 ]+', ' ', temp)
                temp = temp.split()
                key_name = "news"+str(file_count)

                dictionary_matrix[key_name] = dict.fromkeys(unique_words, 0)

                for word in unique_words:
                    if (word in set(temp)):
                        dictionary_matrix[key_name][word] = 1

                # Make numpy array and append them
                matrix[file_count -
                       1] = np.array(list(dictionary_matrix[key_name].values()))

                file_count += 1

        # print(dictionary_matrix["news1"].values())

        print("Enter Input to Search in News")
        user_input = input().lower().split()
        if(user_input == []):
            print("No data to show")
            return

        user_query = dict.fromkeys(unique_words, 0)
        for word in unique_words:
            if (word in set(user_input)):
                user_query[word] = 1

        user_matrix = np.empty([1, len(unique_words)])
        user_matrix = np.array(list(user_query.values()))

        result = matrix.dot(user_matrix)

        result_dict = {}
        for i in range(file_count-1):
            if(result[i] >= 1):
                result_dict[str(i+1)] = int(result[i])

        if(result_dict == {}):
            print("No data found")
            return
        values = sorted(result_dict.values(), reverse=True)
        result_key = []
        to_remove_key = []
        temp = result_dict.copy()
        while(temp != {}):
            for k, v in temp.items():
                if(v == values[0]):
                    result_key.append(k)
                    values.remove(v)
                    to_remove_key.append(k)

            for i in range(len(to_remove_key)):
                temp.pop(to_remove_key[i])
            to_remove_key.clear()

        values = sorted(result_dict.values(), reverse=True)

        with open("url.in") as file:
            url = file.readlines()
            for i in range(len(result_key)):
                print(url[i] + "has score " + str(values[i]))
                print()

    except ConnectionError as ce:
        print("Connection has Lost")
