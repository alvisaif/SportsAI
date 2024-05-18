import xml.etree.ElementTree as ET
import os
import argparse
import cv2

def parse_args():
    parser = argparse.ArgumentParser(description="Visualize Pascal VOC annotations on images.")
    parser.add_argument("--images_dir", required=True, help="Directory containing the images")
    parser.add_argument("--xml_dir", required=True, help="Directory containing the XML annotations")
    parser.add_argument("--output_dir", required=True, help="Directory to save annotated images")
    return parser.parse_args()
def draw_annotations(image_path, xml_path, output_path):
    img = cv2.imread(image_path)
    if img is None:
        print(f"Image {image_path} not found.")
        return
    tree = ET.parse(xml_path)
    root = tree.getroot()
    for obj in root.findall('object'):
        class_name = obj.find('name').text
        bbox = obj.find('bndbox')
        xmin = int(bbox.find('xmin').text)
        ymin = int(bbox.find('ymin').text)
        xmax = int(bbox.find('xmax').text)
        ymax = int(bbox.find('ymax').text)
        img = cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (255, 0, 0), 2)
        cv2.putText(img, class_name, (xmin, ymin-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
    cv2.imwrite(output_path, img)
def main():
    args = parse_args()
    os.makedirs(args.output_dir, exist_ok=True)
    all_xml_files = [f for f in os.listdir(args.xml_dir) if f.endswith('.xml')]
    for xml_file in all_xml_files:
        base_name = xml_file.replace('.xml', '')
        image_name = f"{base_name}.png"  # adjust this if your image extension differs
        image_path = os.path.join(args.images_dir, image_name)
        xml_path = os.path.join(args.xml_dir, xml_file)
        output_path = os.path.join(args.output_dir, image_name)
        draw_annotations(image_path, xml_path, output_path)
        print(f"Annotated image saved to {output_path}")
if __name__ == "__main__":
    main()



    #python visualize_xml_anutation.py --images_dir images/V-BFRD-BF-2024-02-14-0004-000383-T4CCTV1.HR --xml_dir xml_labels --output_dir test_t4