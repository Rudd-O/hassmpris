ROOT_DIR := $(shell dirname "$(realpath $(MAKEFILE_LIST))")

.PHONY = proto clean

proto: \
        src/hassmpris/proto/mpris_grpc.py \
        src/hassmpris/proto/mpris_pb2.py \
        src/hassmpris/proto/mpris_pb2_grpc.py \
        src/hassmpris/proto/__init__.py

test:
	cd $(ROOT_DIR) && \
	tox --current-env

clean:
	rm -f src/hassmpris/proto/mpris_pb2.py
	rm -f src/hassmpris/proto/mpris_grpc.py
	rm -f src/hassmpris/proto/mpris_pb2_grpc.py
	
src/hassmpris/proto/mpris_pb2.py src/hassmpris/proto/mpris_grpc.py src/hassmpris/proto/mpris_pb2_grpc.py: src/hassmpris/proto/mpris.proto
	python3 -m grpc_tools.protoc \
	  src/hassmpris/proto/mpris.proto \
	  --experimental_allow_proto3_optional \
	  --proto_path=src/hassmpris/proto \
	  --grpc_python_out=src/hassmpris/proto \
	  --grpclib_python_out=src/hassmpris/proto \
	  --python_out=src/hassmpris/proto
	sed -i 's/import mpris_pb2 as mpris__pb2/from hassmpris.proto import mpris_pb2 as mpris__pb2/' src/hassmpris/proto/mpris_pb2_grpc.py
	sed -i 's/import mpris_pb2/from hassmpris.proto import mpris_pb2/' src/hassmpris/proto/mpris_grpc.py

src/hassmpris/proto/__init__.py:
	touch $@
