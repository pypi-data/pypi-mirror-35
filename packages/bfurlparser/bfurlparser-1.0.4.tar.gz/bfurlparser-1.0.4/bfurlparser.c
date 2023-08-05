#include <Python.h>

static char module_docstring[] =
    "A blazing fast URL parse.";
static char urlparse_docstring[] =
    "Parses a URL passed as an argument and returns a dictionary with the URL parts.";

static PyObject *bfurlparser_urlparse(PyObject *self, PyObject *args);

static PyMethodDef module_methods[] = {
    {"urlparse", bfurlparser_urlparse, METH_VARARGS, urlparse_docstring},
    {NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC initbfurlparser(void)
{
    PyObject *m = Py_InitModule3("bfurlparser", module_methods, module_docstring);
    if (m == NULL)
        return;
}

static PyObject *bfurlparser_urlparse(PyObject *self, PyObject *args)
{

    char
        *url  = NULL,
        *p    = NULL,
        *prev,
        prevChr;

    int
        hasPort   = 0,
        hasQuery  = 0,
        hasFrag   = 0,
        invPort   = 0;

    PyObject
        *strProto = NULL,
        *strHost  = NULL,
        *strPort  = NULL,
        *strPath  = NULL,
        *strQuery = NULL,
        *strFrag  = NULL;

    // Parse the input tuple
    if (!PyArg_ParseTuple(args, "s", &url))
        return NULL;

    // Locate the protocol ending character
    prev = url;
    for ( p = url ; *p ; p++ ) {
        if ( *p == ':' ) {
            if ( strncmp(p + 1, "//", 2) != 0 ) {
                p++;
                continue;
            }
            *p = 0;
            strProto = PyString_FromString(prev);
            *p = ':';
            break;
        }
    }
    if ( !strProto )
        return NULL;

    // Locate the host end
    p += 3;
    prev = p;
    for ( ; *p && *p != '/' && *p != '#' ; p++ ) {
        if ( *p == ':' ) {
            hasPort = 1;
            break;
        }
    }
    prevChr = *p;
    *p = 0;
    strHost = PyString_FromString(prev);
    *p = prevChr;

    // Locate the port end
    if ( hasPort ) {
        prev = ++p;
        for ( ; *p && *p != '/' && *p != '#'; p++ ) {
            if ( *p < '0' || *p > '9' ) {
                Py_DECREF(strProto);
                Py_DECREF(strHost);
                return NULL;
            }
        }
        prevChr = *p;
        *p = 0;
        strPort = PyString_FromString(prev);
        *p = prevChr;
    }
    else {
        strPort = PyString_FromString("");
    }

    // Locate the path end
    prev = p;
    for ( ; *p ; p++ ) {
        if ( *p == '?' ) {
            hasQuery = 1;
            break;
        }
#ifndef BFURLPARSER_FRAG_AS_PATH
        else if ( *p == '#' ) {
            hasFrag = 1;
            break;
        }
#endif
    }
    prevChr = *p;
    *p = 0;
    strPath = PyString_FromString(*prev ? prev : "/");
    *p = prevChr;

    // Locate the query end (in case we have a query)
    if ( hasQuery ) {
        prev = p;
        for ( ; *p ; p++ ) {
            if ( *p == '#' ) {
                hasFrag = 1;
                break;
            }
        }
        prevChr = *p;
        *p = 0;
        strQuery = PyString_FromString(prev);
        *p = prevChr;        
    }
    else
        strQuery = PyString_FromString("");

    // Locate the fragment end (in case we have a fragment)
    if ( hasFrag ) {
        prev = p;
        for ( ; *p ; p++ );
        strFrag = PyString_FromString(prev);
    }
    else
        strFrag = PyString_FromString("");

    // Build the return value
    PyObject *ret = Py_BuildValue(
        "{s:s,s:s,s:s,s:s,s:s,s:s}",
        "proto",    PyString_AS_STRING(strProto),
        "hostname", PyString_AS_STRING(strHost),
        "port",     PyString_AS_STRING(strPort),
        "path",     PyString_AS_STRING(strPath),
        "query",    PyString_AS_STRING(strQuery),
        "fragment", PyString_AS_STRING(strFrag)
    );

    // Decrement the refcount on them all
    Py_DECREF(strProto);
    Py_DECREF(strHost);
    Py_DECREF(strPort);
    Py_DECREF(strPath);
    Py_DECREF(strQuery);
    Py_DECREF(strFrag);

    return ret;
}


