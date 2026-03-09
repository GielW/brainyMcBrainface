# Dart / Flutter — Language Skill

> Activate for projects using Flutter/Dart (e.g., ilumenTool).

## Style

- **Dart SDK**: `>=3.2.0 <4.0.0` (null-safe)
- **Files**: `snake_case.dart` — enforced across all `lib/` files
- **Classes**: `PascalCase`
- **Functions/variables**: `camelCase`
- **Constants**: `camelCase` or `UPPER_SNAKE_CASE` for compile-time consts

## Tools

| Tool | Purpose | Command |
|------|---------|---------|
| `flutter analyze` | Lint + static analysis | `flutter analyze` |
| `dart format` | Code formatting | `dart format lib/` |
| `flutter test` | Test runner | `flutter test` |
| `flutter pub get` | Install dependencies | `flutter pub get` |

## Linting

- Base config: `package:flutter_lints/flutter.yaml` in `analysis_options.yaml`
- Noisy rules can be disabled per project, but aim to re-enable incrementally
- **Target: 0 errors, 0 warnings** before every commit
- Exclude legacy/archived directories from analysis

## Imports

Always use **package imports** (not relative paths):

```dart
// ✅ Good
import 'package:myapp/services/auth_service.dart';

// ❌ Bad
import '../services/auth_service.dart';
```

## State Management

- Simple projects: `setState()` + `ChangeNotifier`
- Complex projects: Riverpod or Bloc (per project decision)

## Platform-Specific Code

- Always handle both Linux (`/`) and Windows (`\\`) paths
- Use the `path` package for cross-platform path manipulation
- Use `Platform.isLinux`, `Platform.isWindows` guards for platform-specific logic

## Process Execution

For CLI tool wrappers (esptool, avrdude, etc.):

- **Short operations**: `Process.run()` (blocking, collects output)
- **Long operations with progress**: `Process.start()` with streamed stdout/stderr
- Linux: Use `stdbuf -o0 -e0` for unbuffered output piping
- Always `await exitCode` to release resources (USB ports, file handles)

## Build & Run

```bash
cd <flutter_project_root>
flutter pub get                    # Install deps
flutter run -d linux               # Run Linux
flutter run -d windows             # Run Windows
flutter build linux --release      # Build release Linux
flutter build windows --release    # Build release Windows
```

### Linux Build Dependencies

```bash
sudo apt install clang cmake ninja-build pkg-config libgtk-3-dev liblzma-dev \
  libstdc++-12-dev libsecret-1-dev libjsoncpp-dev libudev-dev libserialport-dev
```
