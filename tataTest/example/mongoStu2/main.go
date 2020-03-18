package main

import (
	"context"
	"fmt"
	"time"

	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

func MongoDb() (*mongo.Collection, *context.Context) {
	const (
		port       = 27017
		db         = "test"
		collection = "log"
	)
	ctx, _ := context.WithTimeout(context.Background(), time.Second*10)
	client, _ := mongo.Connect(ctx, options.Client().ApplyURI(fmt.Sprintf("mongodb://localhost:%d", port)))
	collec := client.Database(fmt.Sprintf("%s", db)).Collection(fmt.Sprintf("%s", collection))
	return collec, &ctx
}

func FindData() {

}

func main() {
	collection, ctx := MongoDb()
	res, _ := collection.InsertOne(*ctx, bson.M{"hello": "lei"})
	fmt.Println(res)

}
