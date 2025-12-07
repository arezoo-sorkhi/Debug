


# Structural
"""
real_samples_labels = torch.ones((batch_size, 1))
generated_samples_labels = torch.zeros((batch_size, 1))
But the last batch in the dataset may not have exactly batch_size samples. For example, if batch_size=64 and the number of training images isn’t a multiple of 64, the last batch is smaller.

This makes the size of your labels different from the size of your actual data, causing an error.

Use the actual number of samples in the batch:

real_samples_labels = torch.ones((real_samples.size(0), 1))
generated_samples_labels = torch.zeros((real_samples.size(0), 1))
latent_space_samples = torch.randn((real_samples.size(0), 100)) 
"""



# Cosmetic 

"""
call tight_layout() before suptitle(). This can make the title overlap with the images.

Fix: put suptitle() after tight_layout() and move it a little higher:

"""




# Cosmetic
"""
cmap="gray_r", which reverses the colors. 
Usually cmap="gray" looks better.
"""