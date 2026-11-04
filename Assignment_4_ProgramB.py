# Program Name: Assignment_4_ProgramB.py
# Course: IT3883/Section 01
# Student Name: Ceejay Raut
# Assignment Number: Lab4 A
# Due Date: 11/04/2026
# Purpose: 1.	Program A will prompt the user to type in a string then transmit that string over a socket to program B. Program A will then listen for a response from program B and print to the console whatever was received.
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
                    response = "Message received loud and clear!"  #prepare a response message
                    conn.sendall(response.encode())  #send the response back to Program A

    except Exception as e:  #catch any exception that occurs during execution
        print("An error occurred:", e)

if __name__ == "__main__":
    main()

    