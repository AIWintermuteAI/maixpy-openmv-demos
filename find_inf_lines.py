#find infinite lines
import video, sensor, image, lcd, time
enable_lens_corr = True
lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)
sensor.skip_frames(time = 2000)

v = video.open("/sd/capture_inf_lines.avi", record=1, interval=200000, quality=50)
min_degree = 0
max_degree = 179
tim = time.ticks_ms()

while(time.ticks_diff(time.ticks_ms(), tim)<30000):
    img = sensor.snapshot()
    for l in img.find_lines(threshold = 4000, theta_margin = 25, rho_margin = 25):
        if (min_degree <= l.theta()) and (l.theta() <= max_degree):
            img.draw_line(l.line(), color = (255, 0, 0))
            print(l)	
    lcd.display(img)
    img_len = v.record(img)
print("finish")
v.record_finish()
lcd.clear()
