ROOT_DIR := ../..
INSTALL_HEADERS_DIR := $(ROOT_DIR)/include
INSTALL_LIB_DIR := $(ROOT_DIR)/lib
INSTALL_BIN_DIR := $(ROOT_DIR)/bin
UTILS_DIR := $(ROOT_DIR)/utils
IO_DIR := $(ROOT_DIR)/io

include $(ROOT_DIR)/theory.options $(ROOT_DIR)/common.mk
LIBNAME:= findgroups
LIBRARY := lib$(LIBNAME).a
LIBSRC := findgroups.c findgroups_impl_double.c findgroups_impl_float.c \
         $(UTILS_DIR)/gridlink_impl_double.c $(UTILS_DIR)/gridlink_impl_float.c \
         $(UTILS_DIR)/utils.c $(UTILS_DIR)/progressbar.c $(UTILS_DIR)/cpu_features.c
LIBRARY_HEADERS := $(LIBNAME).h

TARGET := fof
TARGETSRC := fof.c $(IO_DIR)/io.c $(IO_DIR)/ftread.c $(LIBSRC)

INCL   := fof_kernels_double.c fof_kernels_float.c fof_kernels.c.src findgroups.h \
          findgroups_impl_float.h findgroups_impl_double.h findgroups_impl.h.src \
          $(UTILS_DIR)/gridlink_impl_float.h $(UTILS_DIR)/gridlink_impl_double.h $(UTILS_DIR)/gridlink_impl.h.src \
          $(UTILS_DIR)/cellarray_double.h $(UTILS_DIR)/cellarray_float.h $(UTILS_DIR)/cellarray.h.src \
          $(UTILS_DIR)/avx_calls.h $(UTILS_DIR)/sse_calls.h $(UTILS_DIR)/function_precision.h $(UTILS_DIR)/defs.h $(UTILS_DIR)/cpu_features.h \
          $(IO_DIR)/ftread.h $(IO_DIR)/io.h $(UTILS_DIR)/utils.h $(UTILS_DIR)/sglib.h $(UTILS_DIR)/progressbar.h \
		  $(UTILS_DIR)/weight_functions_double.h $(UTILS_DIR)/weight_functions_float.h $(UTILS_DIR)/weight_functions.h.src \
		  $(UTILS_DIR)/weight_defs_double.h $(UTILS_DIR)/weight_defs_float.h $(UTILS_DIR)/weight_defs.h.src


TARGETOBJS  := $(TARGETSRC:.c=.o)
LIBOBJS := $(LIBSRC:.c=.o)

all: $(TARGET) $(TARGETOBJS) $(TARGETSRC) $(ROOT_DIR)/theory.options $(ROOT_DIR)/common.mk Makefile 

findgroups_impl_float.o:findgroups_impl_float.c findgroups_impl_float.h fof_kernels_float.c $(UTILS_DIR)/gridlink_impl_float.h  $(UTILS_DIR)/cellarray_float.h
findgroups_impl_double.o:findgroups_impl_double.c findgroups_impl_double.h fof_kernels_double.c $(UTILS_DIR)/gridlink_impl_double.h  $(UTILS_DIR)/cellarray_double.h
findgroups.o:findgroups.c findgroups_impl_double.h findgroups_impl_float.h
findgroups_impl_float.c findgroups_impl_double.c:findgroups_impl.c.src $(INCL)

libs: lib
lib: $(LIBRARY) 
install:$(INSTALL_BIN_DIR)/$(TARGET) $(INSTALL_LIB_DIR)/$(LIBRARY) $(INSTALL_HEADERS_DIR)/$(LIBRARY_HEADERS)
clean:
	$(RM) $(TARGETOBJS) $(TARGET) $(LIBRARY) fof_kernels_float.c fof_kernels_double.c findgroups_impl_double.[ch] findgroups_impl_float.[ch]
	$(RM) -R *.dSYM

distclean:clean
	cd $(INSTALL_HEADERS_DIR) && $(RM) $(LIBRARY_HEADERS)
	cd $(INSTALL_LIB_DIR) && $(RM) $(LIBRARY)
	cd $(INSTALL_BIN_DIR) && $(RM) $(TARGET)

tests: tests_periodic 

tests_periodic: 
	$(MAKE) -C ../tests fof

include $(ROOT_DIR)/rules.mk


