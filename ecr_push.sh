#!/bin/bash

IMAGE="mock_partner_transaction:latest"
IMAGE_ECR="373686486237.dkr.ecr.us-east-1.amazonaws.com/mock-partner-transaction"
AWS_PROFILE="brinks"

./build.sh

$(aws ecr get-login --no-include-email --region us-east-1 --profile $AWS_PROFILE)

docker tag $IMAGE $IMAGE_ECR
docker push $IMAGE_ECR
