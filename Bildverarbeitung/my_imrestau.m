% Beispiel-Skript zur Demonstration der Bildrestaurierung

A = phantom(256);

%A = imread('cameraman.tif');
A = double(A);
imagesc(A);
colormap gray
pause;

m11 = ones(11) * 1/121;        %Mittelwert-Filter im Ortsraum
B = conv2(A,m11,'same');        % Filterung im Ortsraum (Faltung)
imagesc(B)
pause;

ftA = my_fft2(A);                  % Uebertragung von A in den Fourierraum

imagesc(log(abs(ftA)))
pause;

M11 = zeros(256);               % Mittelwertfilter in den Fourierraum uebertragen
M11(124:134,124:134) = m11;
ftM11 = my_fft2(M11);
imagesc(abs(ftM11));
pause;

ftC = ftA .* ftM11;             % Filterung im Fourierraum (Multiplikation)
imagesc(abs(ftC));
imagesc(log(abs(ftC)));
pause;

C = my_ifft2(ftC);      % Ruecktransformation in den Ortsraum
imagesc(C);
pause;

ftIM11 = zeros(256);            % Generierung des inversen Filters im Fourierraum
ftIM11(abs(ftM11)>0.00001) = 1 ./ (ftM11(abs(ftM11)>0.00001)); % Kehrwert der Frequenzen

ftD = ftC .* ftIM11;            % Filterung mit dem inversen Filter (Multiplikation im Fourierraum)
D = my_ifft2(ftD);      % Ruecktransformation in den Ortsraum
imagesc(D);