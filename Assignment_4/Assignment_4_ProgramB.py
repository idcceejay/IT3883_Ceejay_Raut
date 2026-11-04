# Program Name: Assignment_4_ProgramB.py
# Course: IT3883/Section 01
# Student Name: Ceejay Raut
# Assignment Number: Lab4 B
# Due Date: 11/04/2026
# Purpose: Program B listens for a string from Program A, converts it to all upper case, and sends it back.
# Resources: Claude (debugging hints, comment cleanup), Turbo AI (learning), GitHub (code snippets for arguments and parameters)




import socket

Host = 'localhost'
Port = 12345


def main():
    try:
        #create a tcp socket (ipv4, tcp) that closes with 'with' statement
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((Host, Port))  #bind the socket to the host and port
            s.listen()  #listen for incoming connections
            print("Program B is listening for incoming connections...")
            
            conn, addr = s.accept()  #accept a connection from Program A
            with conn:
                print("Connected by", addr)
                data = conn.recv(1024)  #receive data from Program A
                if data:
                    print("Received from Program A:", data.decode())  #print the received data
                    response = data.decode().upper()  #convert the received string to all upper case
                    conn.sendall(response.encode())  #send the upper case string back to Program A

    except Exception as e:  #catch any exception that occurs during execution
        print("An error occurred:", e)

if __name__ == "__main__":
    main()

    