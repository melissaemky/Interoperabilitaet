function [ftA] = my_fft2(A)
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
ftA = fftshift(fft2(fftshift(A)));
end
