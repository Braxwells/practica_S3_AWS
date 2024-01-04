#!/bin/bash


aws s3api create-bucket \
  --bucket ml-practica-serviciosnube \
  --region eu-south-2 \
  --create-bucket-configuration LocationConstraint=eu-south-2

