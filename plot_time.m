table = import_data('results_table.txt', 1);
idfs_time = table.IDFStime;
a_star_time = table.Atime;
time = zeros(length(idfs_time), 2);

for i = 1:length(idfs_time)
   time(i, 1) = idfs_time(i);
   time(i, 2) = a_star_time(i);
end

figure(1)
plot(time, 'LineWidth', 2)
set(gca,'Yscale','log')
nodes = table.Depth';
xticks(nodes)
legend('IDFS', 'A*', 'location', 'best', 'FontSize', 18)
title('Computation time versus number of bridges in the puzzle', 'FontSize', 16)
ylabel('Computation time [s]', 'FontSize', 18)
xlabel('Number of bridges', 'FontSize', 18)

idfs_nodes = table.IDFSnodes;
a_star_nodes = table.Anodes;
nodes = zeros(length(idfs_nodes), 2);
for i = 1:length(idfs_nodes)
   nodes(i, 1) = idfs_nodes(i);
   nodes(i, 2) = a_star_nodes(i);
end



figure(2)
disp(nodes)
plot(nodes, 'LineWidth', 2)
set(gca,'Yscale','log')
nodes = table.Depth';
xticks(nodes)
legend('IDFS', 'A*', 'location', 'best', 'FontSize', 18)
title('Number of nodes visited versus number of bridges in the puzzle', 'FontSize', 12)
ylabel('Number of nodes', 'FontSize', 18)
xlabel('Number of bridges', 'FontSize', 18)

