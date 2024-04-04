md 代码块

`sdfsdfsdsdfsf`

`sdfsdf`

asdasdas

```c

  int n = 16 * 1024 * 1024;//16mb
  int nbytes = n * sizeof(int);
  int value = 26;

  // allocate host memory
  int *a = 0;
  checkCudaErrors(cudaMalloc
Host((void **)&a, nbytes));
  memset(a, 0, nbytes);

  // allocate device memory
  int *d_a = 0;
  checkCudaErrors(cudaMalloc((void **)&d_a, nbytes));
  checkCudaErrors(cudaMemset(d_a, 255, nbytes));


//=============release resorces===================
  checkCudaErrors(cudaFreeHost(a));
  checkCudaErrors(cudaFree(d_a));


```

asdasdasdasd
asdfasdasda


asdasd
