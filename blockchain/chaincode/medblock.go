package main

import (
	"encoding/json"
	"fmt"
	"github.com/hyperledger/fabric-contract-api-go/contractapi"
)

type SmartContract struct {
	contractapi.Contract
}

type TrialRecord struct {
	ID    string `json:"id"`
	Title string `json:"title"`
	Hash  string `json:"hash"`
}

func (s *SmartContract) RegisterTrial(ctx contractapi.TransactionContextInterface, id string, title string, hash string) error {
	trial := TrialRecord{
		ID:    id,
		Title: title,
		Hash:  hash,
	}
	trialJSON, _ := json.Marshal(trial)
	return ctx.GetStub().PutState(id, trialJSON)
}

func (s *SmartContract) QueryTrial(ctx contractapi.TransactionContextInterface, id string) (*TrialRecord, error) {
	trialJSON, err := ctx.GetStub().GetState(id)
	if err != nil {
		return nil, err
	}
	if trialJSON == nil {
		return nil, fmt.Errorf("trial %s not found", id)
	}
	var trial TrialRecord
	json.Unmarshal(trialJSON, &trial)
	return &trial, nil
}

func main() {
	chaincode, _ := contractapi.NewChaincode(&SmartContract{})
	chaincode.Start()
}