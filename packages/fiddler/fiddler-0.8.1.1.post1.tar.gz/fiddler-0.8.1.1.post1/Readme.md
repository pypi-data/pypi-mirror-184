Fiddler Client
=============

Python client for interacting with Fiddler. Provides a user-friendly interface to our REST API and enables event
publishing for use with our monitoring features.

Requirements
------------
Requires Python >= Python-3.6.3.

Installation
------------

    $ pip3 install fiddler

API Example Usage
-------------
Documentation for the API can be found [here](https://api.fiddler.ai/#introduction). For examples of interacting with our APIs, please check out our [Quick Start Guide](https://docs.fiddler.ai/quick-start/) as well as the work notebooks found on our [Samples Github](https://github.com/fiddler-labs/fiddler-samples).


Version History
-------------
### 0.8.1.1.post1
   - ##### **Modifications**
      - Add model validation in upload_model_package flow.
      - Add nice output formatting for `api.run_feature_importance` for models with text inputs.

### 0.8.1.1
   - ##### **Modifications**
      - change the dependecy of requests package to 0.25.1

### 0.8.1
   - ##### **Modifications**
      - Improved `SegmentInfo` validation.
      - make the dependency versions less strict.

### 0.8.0
   - ##### **New Features**
       - New `publish_events_batch_schema` API call, Publishes a batch events object to Fiddler Service using the passed `publish_schema` as a template.
       - New Ranking Monitoring capability available with publish_events_batch API
   - ##### **Modifications**
      - Enforced package versions in setup.py
      - `trigger_pre_computation` has an additional optional argument (`cache_dataset`) to enable/disable dataset histograms caching.
      - `register_model` has 3 additional optional arguments to enable/disable pdp caching (set to False by default), feature importance caching (set to True by default) and dataset histograms caching (set to True by default).

### 0.7.6
   - ##### **New Features**
       - New segment monitoring related functionality (currently in preview):
          - Ability to create and validate `SegmentInfo` objects,
          - `upload_segment` BE call,
          - `activate_segment` BE call,
          - `deactivate_segment` BE call, and
          - `list_segments` BE call,
   - ##### **Modifications**
       - Upon connecting to the server, the client now performs a version check for the *server* by default. Earlier the default was to only do a version check for the client.

### 0.7.5
   - ##### **New Features**
       - New `update_event` parameter for `publish_events_batch` API.
       - Changes to `fdl.publish_event()`:
           - Renamed parameter `event_time_stamp` to `event_timestamp`
           - Added new parameter: `timestamp_format`
               - Allows specification of timestamp format using the `FiddlerTimestamp` class

### 0.7.4
   - ##### **New Features**
       - New `initialize_monitoring` API call, sets up monitoring for a model. Intended to also work retroactively for legacy schema.
   - ##### **Modifications**
       - Modified `DatasetInfo.from_dataframe` and `ModelInfo.from_dataset_info` to take additional `dataset_id` as parameter.
       - Modified the `outputs` parameter of `ModelInfo.from_dataset_info` to now expect a dictionary in case of regression tasks, specifying output range.
       - Modified the `preferred_explanation_method` parameter of `ModelInfo.from_dataset_info` to accept string names from `custom_explanation_names`. Details in docstring.
       - Misc bug fixes and documentation enhancements.

### 0.7.3
   - ##### **New Features**
       - Changed the default display for `ModelInfo` and `DatasetInfo` to render HTML instead of plaintext, when accessed via jupyter notebooks
       - Added support for GCP Storage ingestion of log events using `fdl.BatchPublishType.GCP_STORAGE`

### 0.7.2
   - ##### **New Features**
       - Restructured the following arguments for `fdl.ModelInfo.from_dataset_info()`
           - Added: `categorical_target_class_details`:
               - Mandatory for Multiclass classification tasks, optional for Binary (unused for Regression)
               - Used to specify the positive class for Binary classification, and the class order for Multiclass classification
           - Modified: `target`:
               - No longer optional, models must specify target columns

### 0.7.1
   - ##### **New Features**
       - Restructured the following arguments for `fdl.publish_events_batch()`
           - Added: `id_field`:
               - Column to extract `id` value from
           - Added: `timestamp_format`:
               - Format of timestamp within batch object. Can be one of:
                    - `fdl.FiddlerTimestamp.INFER`
                    - `fdl.FiddlerTimestamp.EPOCH_MILLISECONDS`
                    - `fdl.FiddlerTimestamp.EPOCH_SECONDS`
                    - `fdl.FiddlerTimestamp.ISO_8601`
           Removed: `default_timestamp`
       - Minor bug fixes
   - ##### **Deprecation Warning**
       - Support `fdl.publish_events_log` and `fdl.publish_parquet_s3` will soon be
         deprecated in favor of `fdl.publish_events_batch()`


### 0.7.0
   - ##### **Dataset Refactor**
       -  Datasets refactored to be members of a Project
           - *This is a change promoting Datasets to be first class within Fiddler. It will affects both the UI and several API in Fiddler*
       - Many API utilizing Projects will now require `project_id` passed as a parameter
   - ##### **New Features**
       - Added `fdl.update_model()` to client
           - *update the specified model, with model binary and package.py from
              the specified model_dir*
       - Added `fdl.get_model()` to client
           - *download the model binary, package.py and model.yaml to the given
              output dir.*
       - Added `fdl.publish_events_batch()` to client
           - *Publishes a batch events object to Fiddler Service.*
           - *Note: Support for other batch methods including `fdl.publish_events_log()`
              and `fdl.publish_parquet_s3()` will be deprecated in the near future
              in favor of `fdl.publish_events_batch()`*
   - ##### **Changes**
       - Simplified logic within `fld.upload-dataset()`
       - Added client/server handshake for checking version compatibilities
           - *Warning issued in case of mismatch*
       - Deleted redundant APIs
           - `fdl.create_surrogate_model()`
           - `fdl.upload_model_sklearn()`
       - Restructured APIs to be more duck typing-friendly (relaxing data type restrictions)
       - Patches for minor bug-fixes


### 0.6.18
   - ##### **Features**
       - Minor updates to ease use of binary classification labels

### 0.6.17
   - ##### **Features**
       - Added new arguments to `ModelInfo.from_dataset_info()`
           - `preferred_explanation_method` to express a preferred default explanation algorithm for a model
           - `custom_explanation_names` to support user-provided explanation algorithms which the user will implement on their model object via package.py.

### 0.6.16
   - ##### **Features**
       - Minor improvements to `publish_events_log()` to circumvent datatype conversion issues

### 0.6.15
   - ##### **Features**
       - Added strict name checks

### 0.6.14
   - ##### **Features**
       - Added client-native multithreading support for `publish_events_log()`
       using new parameters `num_threads` and `batch_size`

### 0.6.13
   - ##### **Features**
       - Added `fdl.generate_sample_events()` to client
         -  *API for generating monitoring traffic to test out Fiddler*
       - Added `fdl.trigger_pre_computation()` to client
         -  *Triggers various precomputation steps within the Fiddler service based on input parameters.*
       -  Optionally add proxies to FiddlerApi() init

### 0.6.12
   - ##### **Features**
       - Added `fdl.publish_parquet_s3()` to client
         -  *Publishes parquet events file from S3 to Fiddler instance.
            Experimental and may be expanded in the future.*

### 0.6.10
   - ##### **Features**
       - Added `fdl.register_model()` to client
           -  *Register a model in fiddler. This will generate a surrogate model,
               which can be replaced later with original model.*
