package utils

import (
	"context"
	"fmt"
	"time"

	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

func MongoDb() (*mongo.Collection, *context.Context) {
	const (
		port   = 27017
		db     = "test"
		collec = "log"
	)
	ctx, _ := context.WithTimeout(context.Background(), time.Second*10)
	client, _ := mongo.Connect(ctx, options.Client().ApplyURI(fmt.Sprintf("mongodb://localhost:%d", port)))
	collection := client.Database(fmt.Sprintf("%s", db)).Collection(fmt.Sprintf("%s", collec))
	return collection, &ctx
}
