// client side

package main

import (
	"log"
	"os"
	"os/signal"

	"github.com/gorilla/websocket"
)

var (
	done      chan interface{}
	interrupt chan os.Signal
)

func recieveHandler(connection *websocket.Conn) {
	defer close(done)
	for {
		_, msg, err := connection.ReadMessage()
		if err != nil {
			log.Println("Error in recieve:", err)
			return
		}
		log.Printf("Recieved: %s\n", msg)
	}
}

func main() {
	done = make(chan interface{})    // channel to indicate reciever handle is done
	interrupt = make(chan os.Signal) // channel to listen for interrupt signal
	signal.Notify(interrupt, os.Interrupt)
}
