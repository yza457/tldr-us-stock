package main

import (
	"log"
	"github.com/streadway/amqp"
	"getdata"
)

func failOnError(err error, msg string) {
	if err != nil {
		log.Fatalf("%s: %s", msg, err)
	}
}


func main() {
	conn, err := amqp.Dial("amqp://guest:guest@localhost:5672/")
	failOnError(err, "Failed to connect to RabbitMQ")
	defer conn.Close()

	ch, err := conn.Channel()
	failOnError(err, "Failed to open a channel")
	defer ch.Close()

	q, err := ch.QueueDeclare(
		"rpc_queue", // name
		false,       // durable
		false,       // delete when unused
		false,       // exclusive
		false,       // no-wait
		nil,         // arguments
	)
	failOnError(err, "Failed to declare a queue")

	err = ch.Qos(
		1,     // prefetch count
		0,     // prefetch size
		false, // global
	)
	failOnError(err, "Failed to set QoS")

	msgs, err := ch.Consume(
		q.Name, // queue
		"",     // consumer
		false,  // auto-ack
		false,  // exclusive
		false,  // no-local
		false,  // no-wait
		nil,    // args
	)
	failOnError(err, "Failed to register a consumer")

	forever := make(chan bool)

	go func() {
		for d := range msgs {
			list := string(d.Body)
			failOnError(err, "Failed to convert body to integer")

			// fmt.Printf("list is %v\n", list)
			response := getdata.GetQuote(list)

			err = ch.Publish(
							"",        // exchange
							d.ReplyTo, // routing key
							false,     // mandatory
							false,     // immediate
							amqp.Publishing{
											ContentType:   "text/plain",
											CorrelationId: d.CorrelationId,
											Body:          []byte(response),
							})
			failOnError(err, "Failed to publish a message")

			d.Ack(false)
		}
	}()

	log.Printf(" [*] Awaiting RPC requests")
	<-forever

	// getdata.GetQuote("['tsla', 'aapl', 'msft', 'goog']");
}