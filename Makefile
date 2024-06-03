# Include directory
INCLUDE_DIR = include

# Compiler flags No warnings allowed for safety
CFLAGS = -Wall -Werror

# Target executable
TARGET = bin/Foo

#Objects, created from src files.
OBJs = $(patsubst src/%.c,obj/%.o,$(wildcard src/*.c))

CC=gcc

# Generate object files
obj/%.o: src/%.c $(INCLUDE_DIR)/Foo.h
	mkdir -p obj
	$(CC) $(CFLAGS) -c $< -I$(INCLUDE_DIR) -o $@

# Link everything together into the executable
# Math.h required.
$(TARGET): $(OBJs)
	mkdir -p bin
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJs) -lm
	
clean:
	rm -f $(OBJs) $(TARGET)
