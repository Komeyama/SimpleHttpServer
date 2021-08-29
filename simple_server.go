package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"net/http/httputil"
)

type Greeting struct {
	Message string `json:"message"`
}

func handler(w http.ResponseWriter, r *http.Request) {
	_, err := httputil.DumpRequest(r, true)
	if err != nil {
		http.Error(w, fmt.Sprint(err), http.StatusInternalServerError)
		return
	}

	var buf bytes.Buffer
	greeting := Greeting{
		Message: "Hello",
	}
	enc := json.NewEncoder(&buf)
	if err := enc.Encode(&greeting); err != nil {
		log.Fatal(err)
	}
	fmt.Fprintf(w, buf.String())
}

func main() {
	var httpServer http.Server
	http.HandleFunc("/greeting", handler)
	log.Println("start http listrning")
	httpServer.Addr = ":8080"
	log.Println(httpServer.ListenAndServe())
}
