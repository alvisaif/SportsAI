import argparse
import cv2
import os

def extract_frames(video_dir_path, save_dir, skip_every=10):
  """Extracts frames from videos in a directory and saves them to a specified directory.

  Args:
      video_dir_path (str): The path to the directory containing video files.
      save_dir (str): The path to the directory where extracted frames will be saved.
      skip_every (int, optional): The number of frames to skip between saving frames. Defaults to 10.
  """

  video_files = [file for file in os.listdir(video_dir_path) if file.endswith('.mp4')]

  for video_name in video_files:
      frame_save_directory = os.path.join(save_dir, video_name[:-4])
      os.makedirs(frame_save_directory, exist_ok=True)

      vidcap = cv2.VideoCapture(os.path.join(video_dir_path, video_name))
      count = 1

      while True:
          success, image = vidcap.read()
          if not success:
              break

          if count % skip_every == 0:
              cv2.imwrite(f"{frame_save_directory}/{video_name.split('.')[0]}_{'0' * (5 - len(str(count))) + str(count)}.png", image)

          print(count, 'Read a new frame: ', success)
          count += 1

      vidcap.release()

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Extract frames from videos.')
  parser.add_argument('--video_dir', type=str, required=True, help='Path to the videos directory.')
  parser.add_argument('--save_dir', type=str, required=True, help='Path to the save directory.')
  parser.add_argument('--skip_every', type=int, default=10, help='Number of frames to skip between saving frames.')
  args = parser.parse_args()

  extract_frames(args.video_dir, args.save_dir, skip_every=args.skip_every)
