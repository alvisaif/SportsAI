import os
import pandas as pd
from argparse import ArgumentParser
from pascal_voc_writer import Writer

def convert_csv_to_xml(labels_dir, xml_save_directory, start_frame_count, end_frame_count):
    os.makedirs(xml_save_directory, exist_ok=True)

    camera_ids_dict = {
        0: 'T1CCTV1',
        1: 'T2CCTV1',
        2: 'T3CCTV1',
        3: 'T4CCTV1',
        4: 'T5CCTVA',
        5: 'T5CCTVB'
    }

    img_h, img_w = 2160, 3840

    for frame_number in range(start_frame_count, end_frame_count + 1):
        for cam_id in range(6):
            file_name = f"camera_id_{cam_id}_{'0' * (8 - len(str(frame_number))) + str(frame_number)}.csv"
            frame_data = pd.read_csv(os.path.join(labels_dir, file_name), header=None)
            
            save_file_name = f'V-BFRD-BF-2024-02-14-0004-000383-{camera_ids_dict[cam_id]}_{"0" * (5 - len(str(frame_number))) + str(frame_number)}'
            
            writer = Writer(os.path.join('images', save_file_name + '.png'), img_w, img_h)
            for (x1, y1, w, h) in frame_data.values[:, 2:6]:
                x2, y2 = x1 + w, y1 + h
                writer.addObject('Player', int(x1), int(y1), int(x2), int(y2))

            writer.save(os.path.join(xml_save_directory, save_file_name + '.xml'))

if __name__ == "__main__":
    parser = ArgumentParser(description="Convert CSV data to Pascal VOC XML format.")
    parser.add_argument("--labels_dir", required=True, help="Directory where labels (and CSV files) are stored.")
    parser.add_argument("--xml_dir", required=True, help="Directory where XML files will be saved.")
    parser.add_argument("--start_frame", type=int, required=True, help="Start frame count.")
    parser.add_argument("--end_frame", type=int, required=True, help="End frame count.")
    
    args = parser.parse_args()

    convert_csv_to_xml(args.labels_dir, args.xml_dir, args.start_frame, args.end_frame)
