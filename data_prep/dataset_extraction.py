import os
import shutil

def extract_dataset(raw_dir, output_dir, is_training=True):
    os.makedirs(output_dir, exist_ok=True)

    for case_folder in os.listdir(raw_dir):
        case_path = os.path.join(raw_dir, case_folder)
        if not os.path.isdir(case_path):
            continue

        target_dir = os.path.join(output_dir, case_folder)
        os.makedirs(target_dir, exist_ok=True)

        for filename in os.listdir(case_path):
            src_file = os.path.join(case_path, filename)

            if "seg" in filename and is_training:
                dst_file = os.path.join(target_dir, "seg.nii.gz")
            elif "t1c" in filename:
                dst_file = os.path.join(target_dir, "t1ce.nii.gz")
            elif "t1n" in filename:
                dst_file = os.path.join(target_dir, "t1n.nii.gz")
            elif "t2f" in filename:
                dst_file = os.path.join(target_dir, "t2f.nii.gz")
            elif "t2w" in filename:
                dst_file = os.path.join(target_dir, "t2w.nii.gz")
            else:
                continue

            shutil.copyfile(src_file, dst_file)

    print(f"{'Training' if is_training else 'Validation'} set extracted to {output_dir}")


if __name__ == "__main__":
    extract_dataset(
        raw_dir="data_prep/dataset/raw_training_set", 
        output_dir="data_prep/dataset/extracted_training_set",
        is_training=True
    )

    extract_dataset(
        raw_dir="data_prep/dataset/raw_validation_set",
        output_dir="data_prep/dataset/extracted_validation_set",
        is_training=False
    )
