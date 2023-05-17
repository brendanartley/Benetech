from benetech_pl.train import train
import argparse
from types import SimpleNamespace

# defaults
config = SimpleNamespace(
    data_dir = "/data/bartley/gpu_test/bartley-benetech-resized/",    
    # data_dir = "/data/bartley/gpu_test/bartley-benetech-resized-small/",
    model_save_dir = "/data/bartley/gpu_test/models/",
    model_path = "google/deplot",
    processor_path = "google/deplot",
    project = "Benetech",
    save_model = True,
    max_patches = 1024,
    max_length = 512,
    batch_size = 3,
    epochs = 1,
    learning_rate = 1e-5,
    verbose = 2,
    num_workers = 4,
    seed = 0,
    # -- Trainer Config --
    accelerator = "gpu",
    fast_dev_run = False,
    overfit_batches = 0,
    devices = 1,
    precision = 32,
    log_every_n_steps = 10,
    accumulate_grad_batches = 1,
)

def parse_args():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--fast_dev_run', action='store_true', help='Check PL modules are set up correctly.')
    parser.add_argument("--seed", type=int, default=config.seed, help="Seed for reproducability.")
    parser.add_argument("--batch_size", type=int, default=config.batch_size, help="Num data points per batch.")
    parser.add_argument("--accumulate_grad_batches", type=int, default=config.accumulate_grad_batches, help="Number of steps before each optimizer step.")
    parser.add_argument("--max_patches", type=int, default=config.batch_size, help="Max pathches for the pix2sctruct model.")
    args = parser.parse_args()
    
    # Update config w/ parameters passed through CLI
    for key, value in vars(args).items():
        setattr(config, key, value)

    return config

def main(config):
    module = train(config)
    pass

if __name__ == "__main__":
    config = parse_args()
    main(config)
