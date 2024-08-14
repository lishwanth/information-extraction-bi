from transformers import LayoutLMForTokenClassification, LayoutLMTokenizerFast, Trainer, TrainingArguments
import torch

class InformationExtractor:
    def __init__(self, model_path=None):
        self.tokenizer = LayoutLMTokenizerFast.from_pretrained('microsoft/layoutlm-base-uncased')
        self.model = LayoutLMForTokenClassification.from_pretrained(model_path if model_path else 'microsoft/layoutlm-base-uncased')

    def predict(self, document):
        inputs = self.tokenizer(document, return_tensors="pt")
        outputs = self.model(**inputs)
        predictions = torch.argmax(outputs.logits, dim=2)
        return predictions

    def train(self, train_data, labels, output_dir='./models'):
        training_args = TrainingArguments(
            output_dir=output_dir,
            evaluation_strategy="epoch",
            learning_rate=5e-5,
            per_device_train_batch_size=8,
            per_device_eval_batch_size=8,
            num_train_epochs=3,
            weight_decay=0.01,
        )

        trainer = Trainer(
            model=self.model,
            args=training_args,
            train_dataset=train_data,
            eval_dataset=labels,
            tokenizer=self.tokenizer,
        )

        trainer.train()
