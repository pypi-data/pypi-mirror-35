# ckpt2tfserving
a simple tool which can convert tensorflow checkpoint model file to tensorflow serving format.

## usage


    from ckpt2tfserving.tools.convertor import convert_ckpt_2_tfserving

    #paramters
    input_tensor_names = {"image": "Placeholder"}
    output_tensor_names = {"result0": "packed_25", "result1": "cls/prob/Reshape_1", "result2": "bbox/pred/BiasAdd"}
    export_path = "path that you want to export the tfserving model file to"
    signature_key = "the_signature_key"
    ckpt_file_path = "path of your model checkpoint file"
    model_type= "predict"

    #convert
    convert_ckpt_2_tfserving(input_tensor_names, output_tensor_names, export_path, signature_key, ckpt_file_path, model_type)