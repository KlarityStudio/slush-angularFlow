
var gulp = require('gulp'),
    shell = require('gulp-shell'),
    git = require('gulp-git'),
  connect = require('gulp-connect');
 
gulp.task('connect', function() {
  connect.server({
    root: './',
    livereload: true
  });
});
 
gulp.task('html', function () {
  gulp.src('index.html')
    .pipe(connect.reload());
});
 
gulp.task('watch', function () {
  gulp.watch(['scss/**','css/**', 'js/**'], ['scss']);
});

gulp.task('parse', shell.task([
  'python3 ./python/parser.py' ,
  'echo parsed'
]))

gulp.task('pull-webflow', function() {
  git.clone('https://github.com/<%= authorName %>/<%= webflowRepo %>', {args: './Webflow/'}, function(err) {
    if (err) throw err;
  });
});
 
gulp.task('default', ['connect', 'watch', 'parse', 'pull-webflow']);
