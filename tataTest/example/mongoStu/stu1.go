package main

import (
	"context"
	"fmt"
	"log"
	"time"

	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
	"go.mongodb.org/mongo-driver/mongo/readpref"
)

func main() {
	ctx, _ := context.WithTimeout(context.Background(), 10*time.Second)
	client, err := mongo.Connect(ctx, options.Client().ApplyURI("mongodb://localhost:27017"))
	if err != nil {
		log.Fatal(err)
	}
	client.Ping(ctx, readpref.Primary())
	collection := client.Database("test").Collection("log")
	// res, _ := collection.InsertOne(ctx, bson.M{"name": "lei"})
	res, _ := collection.Find(ctx, bson.D{})
	for res.Next(ctx) {
		var result bson.M
		res.Decode(&result)
		fmt.Println(result["name"])
	}
	defer res.Close(ctx)
	client.Disconnect(ctx)
}
