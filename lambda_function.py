import json
import boto3

translate = boto3.client('translate')

def lambda_handler(event, context):
    try:
        if event.get("body") is None:
            return {
                "statusCode": 400,
                "headers": {
                    "Access-Control-Allow-Origin": "*"
                },
                "body": json.dumps({"error": "Missing request body"})
            }

        body = json.loads(event["body"])
        text = body.get("text")
        target_language = body.get("target_language")
        source_language = body.get("source_language")  # optional

        if not text or not target_language:
            return {
                "statusCode": 400,
                "headers": {
                    "Access-Control-Allow-Origin": "*"
                },
                "body": json.dumps({"error": "Missing 'text' or 'target_language'"})
            }

        # Auto-detect if source_language not provided
        if source_language:
            result = translate.translate_text(
                Text=text,
                SourceLanguageCode=source_language,
                TargetLanguageCode=target_language
            )
        else:
            result = translate.translate_text(
                Text=text,
                SourceLanguageCode="auto",
                TargetLanguageCode=target_language
            )

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "POST, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type"
            },
            "body": json.dumps({"translated_text": result["TranslatedText"]})
        }

    except Exception as e:
        print("Error:", str(e))
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"error": "Internal server error"})
        }

