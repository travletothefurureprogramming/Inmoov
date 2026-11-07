from vision.tracker import find_object
from tools import ik
from tools import uart
from inteligence import inteligence
from inteligence import process_command


if __name__ == "__main__":
    while True:
        question = input("Ask something: ")

        response = inteligence.get_answer(question)
        print(response)

        process_command.proccess(response)