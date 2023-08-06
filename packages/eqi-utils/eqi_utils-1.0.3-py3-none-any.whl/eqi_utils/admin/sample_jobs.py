import mmap
import contextlib
import random
import os
import math


def _sample_jobs(filepath, total_to_sample, output_path, seed=None, max_skip=5):
    if total_to_sample <= 0:
        return ''
    job_start_bytes = '<job>'.encode()
    job_end_bytes = '</job>'.encode()
    with open(filepath, 'r') as f:
        with contextlib.closing(
                mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)) as m:
            with open(output_path, 'a') as out_file:
                if seed:
                    random.seed(seed)
                current_total = 0
                while current_total < total_to_sample:
                    skip = random.randint(1, max_skip)
                    job_start_pos = next_pos(m, job_start_bytes, skip)
                    m.seek(job_start_pos)
                    job_end_pos = m.find(job_end_bytes, job_start_pos) + len(
                        job_end_bytes)
                    out_file.write(str(m.read(job_end_pos - job_start_pos),
                                       "utf-8") + '\n')
                    m.seek(job_end_pos)
                    current_total = current_total + 1
    return current_total


def sample_jobs_from_folder(folder, total_to_sample, output_path, seed=None,
                            max_skip=100):
    if not os.path.isdir(folder):
        raise ValueError("{} is not a folder".format(folder))
    files_in_dir = os.listdir(folder)
    total_sampled = 0
    total_per_file = math.ceil(total_to_sample / len(files_in_dir))
    for file in os.listdir(folder):
        num_to_sample = total_per_file
        if total_to_sample - total_sampled < num_to_sample:
            num_to_sample = total_to_sample - total_sampled
        extract_total = _sample_jobs(os.path.join(folder, file),
                                     num_to_sample, output_path, seed=seed,
                                     max_skip=max_skip)
        total_sampled += extract_total
        if total_sampled >= total_to_sample:
            break
    return total_sampled


def append_line(filepath, line):
    with open(filepath, 'a') as out_file:
        out_file.write(line + '\n')


def next_pos(m, id_bytes, skip):
    cnt = 0
    pos = m.tell()
    while cnt < skip and pos != -1:
        pos = m.find(id_bytes, pos)
        cnt += 1
    return m.find(id_bytes, pos)
