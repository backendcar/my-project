clear all
close all
clc
bit = randi([0,1],1024,100);
sym = vec2mat(bit,4);
sym1 = bi2de(sym,'left-msb');
% const = pskmod(sym1,4,pi/4,'gray');
const = qammod(sym1,16,'gray');

scatterplot(const);
% constn = awgn(const,12,"measured");
% scatterplot(constn);
filt = rcosdesign(.05, 6, 5, 'sqrt');
plot(filt)
% hold on
% filt1 = rcosdesign(.75, 6, 5, 'sqrt');
% plot(filt1)
data = upsample(const,5);
signal = conv(data,filt);
pwelch(signal,[],[],[],10e6,'centered');
plot(abs(fftshift(fft(signal))));
