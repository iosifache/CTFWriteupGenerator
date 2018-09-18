# set n(size) and k(block size)
n = 1024 * 750
k = 512

# RAID5 recovery, considering parity bits
with open("disk0", "rb") as f1:
    with open("disk1", "rb") as f2:
        with open("disk2", "rb") as f3:
            with open("disk_out", "wb") as f_out:
                x = 2
                for _ in xrange(n):
                    blocks = (f1.read(k), f2.read(k), f3.read(k))
                    data_blocks = [b for i, b in enumerate(blocks) if i != x]
                    x = (x - 1) % 3
                    f_out.write("".join(data_blocks))