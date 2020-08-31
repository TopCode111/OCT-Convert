from oct_converter.readers import E2E


filepath = '../sample_files/file.e2e'
file = E2E(filepath)
oct_volumes = file.read_oct_volume()  # returns an OCT volume with additional metadata if available

for volume in oct_volumes:
    volume.peek() # plots a montage of the volume
    volume.save('{}.avi'.format(volume.patient_id))
