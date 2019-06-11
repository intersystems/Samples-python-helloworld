# Samples-python-helloworld

This is a simple hello world example to show a Python connection to InterSystems IRIS.

## To run in InterSystems Learning Labs or Evaluator Edition (on AWS, GCP, or Azure)

1. Open Samples-python-helloworld/hello_world.py to see the sample 
2. For AWS, GCP, or Azure ONLY: Modify host to be "try-iris" (Please skip this step if using InterSystems Learning Labs)
3. In the integrated terminal window, type:  

    * `cd /home/project/Samples-python-helloworld`  
    * `pip install wheel/irisnative-1.0.0-cp34-abi3-linux_x86_64.whl`  
    * `python hello_world.py`  
	
## To run locally

1. Clone this repo and open it in your favorite IDE
2. Open Samples-python-helloworld/hello_world.py and verify the values for ip, port, username, and password. Update as needed.
3. In the integrated terminal window, navigate to your repository's home directory and type:  

    * Windows: `pip install wheel irisnative-1.0.0-cp34.cp35.cp36.cp37-none-win_amd64.whl`
    * Mac: `pip install wheel/irisnative-1.0.0-cp34-abi3-macosx_10_13_x86_64.macosx_10_14_x86_64.whl`
    * Linux: `pip install wheel/irisnative-1.0.0-cp34-abi3-linux_x86_64.whl` 

4. Run sample code: `python hello_world.py`  
