# Copyright 2020 NVIDIA
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import torch
import torch.utils.data
import glob
import PIL.Image
import subprocess
import cv2
import os
import uuid
import subprocess


class ImageClassificationDataset(torch.utils.data.Dataset):
    
    def __init__(self, directory, categories, transform=None):
        self.categories = categories
        self.directory = directory
        self.transform = transform
        self._refresh()
    
    
    def __len__(self):
        return len(self.annotations)
    
    
    def __getitem__(self, idx):
        ann = self.annotations[idx]
        image = cv2.imread(ann['image_path'], cv2.IMREAD_REDUCED_GRAYSCALE_8)
        image = PIL.Image.fromarray(image)
        if self.transform is not None:
            image = self.transform(image)
        return image, ann['category_index']
    
    
    def _refresh(self):
        self.annotations = []
        for category in self.categories:
            category_index = self.categories.index(category)
            for image_path in glob.glob(os.path.join(self.directory, category, '*.jpg')):
                self.annotations += [{
                    'image_path': image_path,
                    'category_index': category_index,
                    'category': category
                }]
    
    def save_entry(self, image, category):
        """Saves an image in BGR8 format to dataset for category"""
        if category not in self.categories:
            raise KeyError('There is no category named %s in this dataset.' % category)
            
        filename = str(uuid.uuid1()) + '.jpg'
        category_directory = os.path.join(self.directory, category)
        
        if not os.path.exists(category_directory):
            subprocess.call(['mkdir', '-p', category_directory])
            
        image_path = os.path.join(category_directory, filename)
        cv2.imwrite(image_path, image)
        self._refresh()
        return image_path
    
    def get_count(self, category):
        i = 0
        for a in self.annotations:
            if a['category'] == category:
                i += 1
        return i