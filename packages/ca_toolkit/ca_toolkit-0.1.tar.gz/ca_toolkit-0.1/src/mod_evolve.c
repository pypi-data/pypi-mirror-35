#include <Python.h>
#include <numpy/arrayobject.h>
#include "evolve.h"

#if PY_MAJOR_VERSION >= 3
#define IS_PY3K
#endif // PY_MAJOR_VERSION

static PyObject *
evolve(PyObject *self, PyObject *args)
{
    // arg1: 1D array
    // nrow: nrow
    // ncol: ncol
    // out : updated 1D array
    PyObject *arg1 = NULL, *out = NULL;
    int nrow, ncol;
    PyObject *arr1 = NULL, *oarr = NULL;

    if (!PyArg_ParseTuple(args, "OiiO!", &arg1, &nrow, &ncol, &PyArray_Type, &out))
        return NULL;

    arr1 = PyArray_FROM_OTF(arg1, NPY_INT32, NPY_ARRAY_IN_ARRAY);
    if (arr1 == NULL)
        return NULL;

    oarr = PyArray_FROM_OTF(out, NPY_INT32, NPY_ARRAY_INOUT_ARRAY);
    if (oarr == NULL)
        goto fail;

    int nsize = PyArray_SIZE(arr1);
    npy_int32 *dptr1 = (npy_int32 *)PyArray_DATA(arr1);
    npy_int32 *dptro = (npy_int32 *)PyArray_DATA(oarr);

    int *new_arr = update_pattern(dptr1, nsize, nrow, ncol);

    for (int i = 0; i < nsize; i++)
        dptro[i] = new_arr[i];
    free(new_arr);

    Py_DECREF(arr1);
    Py_DECREF(oarr);
    Py_INCREF(Py_None);

    return Py_None;

fail:
    Py_XDECREF(arr1);
    Py_XDECREF(oarr);
    return NULL;
}

static char evolve_docs[] = "evolve(arr_in, ncol, nrow, arr_out): \n \
\tEvolve one interation, keep results in arr_out.\n";

static PyMethodDef EvolveMethods[] = {
    {"evolve", evolve, METH_VARARGS, evolve_docs},
    {NULL, NULL, 0, NULL}};

#ifdef IS_PY3K
static struct PyModuleDef evolvemodule = {
    PyModuleDef_HEAD_INIT,
    "evolve",
    NULL,
    -1,
    EvolveMethods};

PyMODINIT_FUNC
PyInit_evolve(void)
{
    import_array();
    return PyModule_Create(&evolvemodule);
}

#else
PyMODINIT_FUNC
initevolve(void)
{
    (void)Py_InitModule("evolve", EvolveMethods);
    import_array();
}
#endif
