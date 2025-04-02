def minimum_compressions(n, m, songs):
# Step 1: Calculate total size with   out compression
    total_size = sum(song[0] for song in songs)
    
    # Step 2: If total size is already <= m, no compression is needed
    if total_size <= m:
        return 0
    
    # Step 3: Calculate the potential gain from compression
    gains = []
    for song in songs:
        ai, bi = song
        gains.append(ai - bi)
    
    # Step 4: Sort gains in descending order to compress the largest ones first
    gains.sort(reverse=True)
    
    # Step 5: Try to compress songs one by one, starting from the largest gain
    compressed_size = total_size
    compress_count = 0
    for gain in gains:
        compressed_size -= gain
        compress_count += 1
        
        # If the total size is now within the capacity, return the result
        if compressed_size <= m:
            return compress_count
    
    # Step 6: If we couldn't fit all songs even after full compression
    return -1


# Example usage:
# Read input
n, m = map(int, input().split())
songs = [tuple(map(int, input().split())) for _ in range(n)]

# Call the function to get the minimum compressions needed
result = minimum_compressions(n, m, songs)
print(result)
