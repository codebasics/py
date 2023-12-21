import speedtest


def speedtester():
    st = speedtest.Speedtest()

    print("Loading server list...\n")
    st.get_servers()
    print("Choosing best server...")
    best = st.get_best_server()
    print(f"Found: {best['host']} located in {best['country']}")

    option = int(
        input(
            """What speed do you want to test:  
    
    1) Download Speed  
    
    2) Upload Speed  
    
    3) Ping 
    
    Your Choice: """
        )
    )

    if option == 1:
        print("Performing download test...")
        downloadresult = st.download()
        print(f"Download speed: {downloadresult / 1024 / 1024: .2f} Mbit/s")

    elif option == 2:
        print("Performing upload test...")
        uploadresult = st.upload()
        print(f"Upload result : {uploadresult /1024 /1024:.2f} Mbit/s")

    elif option == 3:
        ping_result = st.results.ping
        print(f"Ping: {ping_result}ms")

    else:
        print("Please enter the correct choice !")


if __name__ == "__main__":
    speedtester()
