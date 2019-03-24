#find non-infinite lines
import video, sensor, image, lcd, time
lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565) # grayscale is faster
sensor.set_framesize(sensor.QVGA)
sensor.run(1)
sensor.skip_frames(30)
v = video.open("/sd/capture_lines.avi", record=1, interval=200000, quality=50)
tim = time.ticks_ms()
while(time.ticks_diff(time.ticks_ms(), tim)<30000):
    img = sensor.snapshot()
    for l in img.find_line_segments(merge_distance = 10, max_theta_diff = 25, roi=(80,60,160,120)):
        img.draw_line(l.line(), color = (255, 0, 0))
    lcd.display(img)
    img_len = v.record(img)
print("finish")
v.record_finish()
lcd.clear()
