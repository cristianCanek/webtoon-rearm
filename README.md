# webtoon-rearm

A simple but useful tool to paste webtoon images when they come split.

## Description

**webtoon-rearm** combines multiple image files (webp, jpg, jpeg, png) into a single tall PNG image. It's perfect for consolidating split webtoon chapters or manga pages into one continuous image.

### Features
- Supports multiple image formats (webp, jpg, jpeg, png)
- Automatically sorts images by filename
- Resizes all images to match the width of the widest image
- Stacks images vertically with consistent width
- Customizable output filename and directory
- Displays loading progress and final dimensions

## Usage

### Basic Usage
```bash
python core.py <images_directory>
```
Saves the combined image as `output.png` in the same directory as the input images.

### Custom Output Filename
```bash
python core.py <images_directory> <filename.png>
```
Saves the combined image with a custom filename in the input directory.

### Custom Output Path
```bash
python core.py <images_directory> <filename.png> <output_directory>
```
Saves the combined image with a custom filename to a specified output directory.

## Example
```bash
python core.py ./chapter_1_images combined_chapter.png ./output
```
This will:
1. Read all images from `./chapter_1_images`
2. Combine them into a single image
3. Save it as `combined_chapter.png` in the `./output` directory
