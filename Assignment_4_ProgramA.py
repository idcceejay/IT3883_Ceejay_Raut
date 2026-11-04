# Program Name: Assignment_4_ProgramA.py
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

    message = input("Enter a string to send to Program B: ")    
    
    try:
        
        #create a tcp socket (ipv4, tcp) that closes with 'with' statement
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((Host, Port))  #connect to the server
            s.sendall(message.encode())  #send the message to the server
            
            response = s.recv(1024)  #receive the response from the server
            print("Received from Program B:", response.decode())  #print the response

    except ConnectionRefusedError: # this exception is raised when the connection is refused, which means that Program B is not running or not accepting connections
        print("Connection refused. Make sure Program B is running.")

if __name__ == "__main__":
    main()

    
                    