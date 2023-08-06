# Copyright (c) 2021-2022 Intel Corporation
#
# Copyright 2015 The TensorFlow Authors. All Rights Reserved.
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
# ==============================================================================
'''version information for Intel ® Extension for TensorFlow*'''

__version__ = '1.1.0'
__git_desc__= 'd4f2f46e'
VERSION = __version__
GIT_VERSION = __git_desc__ if len(__git_desc__) > 8 else 'v' + __version__ + '-' + __git_desc__
COMPILER_VERSION = 'gcc-, dpcpp-2023.0.0.20221201'
ONEDNN_GIT_VERSION = 'v2.7.0-4ee69b1f'
TF_COMPATIBLE_VERSION = '>= 2.8.0'
