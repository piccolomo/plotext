


// Points get_line(const Point & p1, const Point & p2, const bool & last = false) {
//     // Get coordinates
//     float x1 = p1.get_x();
//     float y1 = p1.get_y();
//     float x2 = p2.get_x();
//     float y2 = p2.get_y();

//     // Calculate differences and slope


//     float L = max(abs(Dx), abs(Dy)) + 1;
//     //wcout << L << endl;

//     // Avoid division by zero; if Dx is 0, slope is infinite
//     float s = (Dx != 0) ? Dy / Dx : std::numeric_limits<float>::infinity();

//     // Determine step sizes (default to 1, adjust for HD points)
//     float dx = 1.0f;
//     float dy = 1.0f;
//     if (p1.is_hd()) {
//         dx /= p1.get_cols();
//         dy /= p1.get_rows();}

//     //wcout << p1.is_hd()<< " dx " << dx << " dy " << dy << endl;
//     float ds = dy / dx;

//     // Adjust step direction based on direction of line
//     float sx = (Dx > 0) ? dx : -dx;
//     float sy = (Dy > 0) ? dy : -dy;

//     Points out(L); // Initialize the output Points container
    

//     // Add the first point
//     out.add_point(p1); 
//     //wcout << "a " << s <<" "<<  ds <<" "<< (s / ds < 1) <<endl;

//     // // Skip if p2 is "none" (invalid or placeholder point)
//     // if (p1.is_none() or p2.is_none()) {
//     //     return out;}

//     if (abs(s / ds) < 1) {
//         auto X = range(x1 + sx, x2, sx);
//         for (auto & x : X) {
//             auto y = s * (x - x1) + y1;
//             Point pp(x, y, p1);
//             out.add_point(pp);}} 
//     else {
//         auto Y = range(y1 + sy, y2, sy);
//         for (auto & y : Y) {
//             auto x = (y - y1) / s + x1;
//             Point pp(x, y, p1);
//             out.add_point(pp);}}

//         //wcout << "b" << endl;
//     // Add the second point
//     if (last) {out.add_point(p2);}
//     //wcout << "c" << endl << endl;
//     return out;}