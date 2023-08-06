from functools import partial

from safe_gpu import safe_gpu

import argparse
import torch
import os
import sys

from .model import build_model
from .trainer import Trainer
from .tester import Tester

from .dataset import load_dataset
from .helper import ModelConfig, BERT_BASE_NAME, build_tokenizer


def parse_arguments():
    print(' '.join(sys.argv))

    parser = argparse.ArgumentParser()

    parser.add_argument("--train-bert", action="store_true", default=False, help="Whether to train BERT as well. Note that this extremely increases training time.")
    parser.add_argument("--epochs", type=int, default=1, help="Number of epochs")
    parser.add_argument("--batch-size", type=int, default=32, help="Batch size")
    parser.add_argument("--lr", type=float, default=0.00003, help="Learning rate")
    parser.add_argument("--grad", type=int, default=10, help="Max grad norm")

    parser.add_argument("--sep", action="store_true", default=True, help="Whether to separate lines with [LF] token.")
    parser.add_argument("--sep-loss", action="store_true", default=False, help="Whether to calculate loss on the [LF] token.")
    parser.add_argument("--labels", type=str, default="all", help="'all' or 'subset'")
    parser.add_argument("--format", type=str, default="iob", help="'iob' or 'io'")
    parser.add_argument("--max_len", type=int, default=256, help="Max length of token sequence as bert input")

    parser.add_argument("--model-path", help="Path to a model checkpoint.", default=None)
    parser.add_argument("--bert-path", default=BERT_BASE_NAME, help="Path to a pretrained BERT model. This is NOT used if --model-path is specified.")
    parser.add_argument("--tokenizer-path", default=BERT_BASE_NAME, help="Path to a tokenizer.")
    parser.add_argument("--save-path", help="Path to a directory where checkpoints are stored.")
    parser.add_argument("--save-tokenizer", help="Save tokenizer with model checkpoints", action="store_true", default=False)

    parser.add_argument("--ocr-path", help="Path to either (1) root dir with OCR files or (2) LMDB with texts from OCR")
    parser.add_argument("--train-path", help="Path to a text file with training data.")
    parser.add_argument("--val-path", help="Path to a text file with validation data.")
    parser.add_argument("--test-path", help="Path to a text file with test data.")

    args = parser.parse_args()
    return args


def main():
    args = parse_arguments()

    safe_gpu.claim_gpus()

    model_config = ModelConfig(
        labels=args.labels,
        format=args.format,
        max_len=args.max_len,
        sep=args.sep,
        sep_loss=args.sep_loss
    )

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Device: {device}")

    tokenizer = build_tokenizer(args.tokenizer_path, model_config, add_special=True)
    print("Tokenizer loaded.")

    model = build_model(tokenizer=tokenizer, model_path=args.model_path, pretrained_bert_path=args.bert_path)
    model = model.to(device)
    print("Model loaded.")

    load_data = partial(load_dataset, ocr_path=args.ocr_path, batch_size=args.batch_size, tokenizer=tokenizer, model_config=model_config)

    train_dataset = load_data(args.train_path)
    val_dataset = load_data(args.val_path)
    test_dataset = load_data(args.test_path)
    print("Datasets loaded and DataLoaders created.")

    trainer_settings = {
        "epochs": args.epochs,
        "learning_rate": args.lr,
        "max_grad_norm": args.grad,
        "bert": args.train_bert,
        "output_folder": args.save_path
    }

    os.makedirs(trainer_settings["output_folder"], exist_ok=True)
    print("Output folder created.")

    trainer = Trainer(settings=trainer_settings, model=model, tokenizer=tokenizer)
    print("Trainer created.")

    print("Training starts ...")
    trainer.train(train_dataset, val_dataset)
    print("Training finished.")

    tester = Tester(model)
    print("Tester created.")

    print("Testing starts ...")
    tester.test(test_dataset)
    print("Testing finished.")

    model_config.save(args.save_path)
    print("Model config saved.")

    if args.save_tokenizer:
        tokenizer.save_pretrained(trainer_settings["output_folder"])
        print("Tokenizer saved.")


if __name__ == "__main__":
    main()
