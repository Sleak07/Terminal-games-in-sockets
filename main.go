package main

import (
	"fmt"
	"net/http"

	"github.com/gorilla/websocket"
)

// upgrader to upgrade the HTTps to websockets
var upgrader = websocket.Upgrader{
	CheckOrigin: func(r *http.Request) bool {
		return true
	},
}

func wshandler(w http.ResponseWriter, r *http.Request) {
	conn, err := upgrader.Upgrade(w, r, nil)
	if err != nil {
		fmt.Println("Error upgrading the connection", err)
		return
	}
	defer conn.Close()
	// Listen for incoming messages
	for {
		// Read messages from client
		_, message, err := conn.ReadMessage()
		if err != nil {
			fmt.Println("Error reading the message", err)
			break
		}
		fmt.Printf("Recieved:%s\\n", message)
		// Echo message back to client
		if err := conn.WriteMessage(websocket.TextMessage, message); err != nil {
			fmt.Println("Error writing message:", err)
			break
		}
	}
}

func main() {
	http.HandleFunc("/ws", wshandler)
	fmt.Println("Websocket server started on :8080")
	err := http.ListenAndServe(":8080", nil)
	if err != nil {
		fmt.Println("Error starting the server:", err)
	}
}
